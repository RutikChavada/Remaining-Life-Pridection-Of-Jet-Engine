import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import RULPredictor from './Components/Predect'
import Home from './Components/home/home'
import Navbar from './Components/navbar/navbar'
import{
  createBrowserRouter,
  RouterProvider,
}from "react-router-dom";
import About from './Components/about/about'

function App() {
  const router = createBrowserRouter([
    {
      path: "/",
      element: <Navbar/>,
      children: [
        {
          path:"/",
          element:<Home/>
        },
        {
          path:"/pridect",
          element:<RULPredictor/>
        },
        {
          path:"/about",
          element:<About/>
        },
      ]
    },
  ])
  return(
    <RouterProvider router={router}/>
  )
}

export default App
