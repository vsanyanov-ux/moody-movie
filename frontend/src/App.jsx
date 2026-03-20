import { useState } from 'react'
import './App.css'

function App() {
  const [situation, setSituation] = useState('')
  const [loading, setLoading] = useState(false)
  const [movie, setMovie] = useState(null)
  const [error, setError] = useState(null)

  const API_URL = 'https://vladim82-moody-movie-api.hf.space'

  const handleRecommend = async () => {
    if (!situation.trim()) return

    setLoading(true)
    setError(null)
    setMovie(null)

    try {
      const response = await fetch(`${API_URL}/recommend`, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ situation }),
      })

      if (!response.ok) {
        throw new Error('Не удалось получить рекомендацию')
      }

      const data = await response.json()
      setMovie(data)
    } catch (err) {
      setError(err.message)
    } finally {
      setLoading(false)
    }
  }

  return (
    <div className="container">
      <header>
        <h1>Moody Movie</h1>
        <p>Кинопараллель твоей жизни</p>
      </header>

      <main className="input-section">
        <textarea
          placeholder="Опиши свою ситуацию здесь... (например: 'Потерял работу после 10 лет службы, чувствую себя потерянным')"
          value={situation}
          onChange={(e) => setSituation(e.target.value)}
          disabled={loading}
        />
        <button 
          onClick={handleRecommend} 
          disabled={loading || !situation.trim()}
        >
          {loading ? 'Ищем фильм...' : 'Найти фильм'}
        </button>
      </main>

      {loading && <div className="loader"></div>}

      {error && <p style={{ color: '#ff4d4d' }}>{error}</p>}

      {movie && (
        <article className="movie-card">
          <div className="movie-header">
            <span className="movie-badge">Рекомендация</span>
            <h2 className="movie-title">{movie.title}</h2>
            <div className="movie-info">
              <span>{movie.year}</span>
              <span>•</span>
              <span>{movie.country}</span>
            </div>
          </div>
          <div className="movie-body">
            <p className="movie-description">{movie.description}</p>
            <div className="actors-list">
              {movie.actors.map((actor, idx) => (
                <span key={idx} className="actor-chip">{actor}</span>
              ))}
            </div>
          </div>
        </article>
      )}
    </div>
  )
}

export default App
