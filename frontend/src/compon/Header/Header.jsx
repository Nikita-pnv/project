import './Header.css'
import { useState } from 'react';



export function Header (){

  //const now = new Date ();
  const [now, setdate] = useState (new Date)
  setInterval(() => setdate (new Date), 1000)

    return( <nav>
      <h3>Lorem ipsum </h3>
      <span>{now.toLocaleTimeString() }</span>
    </nav>
    )
  }