import { useState } from 'react'
import './App.css'

interface registroPeso{
  id: string,
  peso: number,
  date: string
}

function App() {
  const [peso, setPeso] = useState<number>(0)

  const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
    setPeso(Number(e.target.value));
  }

  const submitPeso = (peso: number) : void =>{
    console.log(`se ha registrado el peso ${peso}`);
  }

  return(
    <div>
      <div>
        setPeso
        <input
          id="pesoInput"
          type="number"
          onChange={handleChange}
          value={peso}
        />
        <button
          onClick={() => submitPeso(peso)}
        >
          registrar peso {peso}
        </button>
      </div>
    </div>
  )
}
export default App
