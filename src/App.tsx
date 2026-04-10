import { useState } from 'react'
import './App.css'

interface PesoTracker{
  peso: number
}

function App() {
  const [count, setCount] = useState(0)
  const [peso, setPeso] = useState<number>(0)

  const 
  return (
    <div>
      <button
        onClick={()=>setCount((count)=>count + 1)}
      >
        valor actual {count}
      </button>
      <button
        onClick={()=>setCount(0)}
      >
        reset
      </button>
    

      <div>
        setPeso
        <button>
          fornai
        </button>
      </div>
    </div>
  )
}
export default App
