 import React, {Component} from "react";
 import "./Header.css"

class Header extends React.Component {
    constructor(props) {
        super(props)
    }
    render() {
        return (
            <nav>
                <ul>
                    <li><a href="/">Blog</a></li>
                    <li><a href="#">Home</a></li>
                    <li><a href="#">Contact us</a></li>
                    <li><a href="#">Topics</a></li>
                </ul>
            </nav>
        )
    }
}

export default Header;