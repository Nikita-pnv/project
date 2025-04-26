import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { Header } from './compon/Header/Header'
import './date'
import { sneakers } from './date'
import Waytodate from './compon/Waytodate/Waytodate'
import RegistrationFrom from './compon/FormReg/FormReg'

export default function App() {
  return(
    <>
    <Header></Header>
    {/* {sneakers.map(sneaker =>  */}
{/*     
    /*map - обращение к каждым данным
      <Waytodate name = {sneaker.name} discr = {sneaker['discr']}/>
      <Waytodate {...sneaker}/>
      
      /*альтернатвиный вариант получения всех данных из данных sneaker */ }
      <RegistrationFrom />

    </>
    )
}

