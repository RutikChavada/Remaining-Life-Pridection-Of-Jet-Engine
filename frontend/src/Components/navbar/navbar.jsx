import React from "react";
import "./navbar.css"
import logo2 from "../../assets/logo2.png";
import { Outlet } from "react-router-dom";

function Navbar(){
    return(
        <>
        <div className="nav">
        <img src={logo2} alt="logo"/>
        <div className="menu">
        <ul>
            <li><a href="/">Home</a></li>
            <li><a href="/pridect">Pridect</a></li>
            <li><a href="/about">About</a></li>
        </ul>
        </div>
        <div className="login">
            <ul>
                <li><a href="#">Sign in</a></li>
                <li><a href="#">Login</a></li>
            </ul>
        </div>
        </div>
        <Outlet/>
        </>
    )
}

export default Navbar;