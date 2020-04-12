 import React, {Component} from "react";
 import "./Header.css"

class Header extends React.Component {
    constructor(props) {
        super(props)
    }
    render() {
        return (
            <nav>
                <a href="#">Blog</a>
                <a href="#">Blog</a>
                <a href="#">Blog</a>
                <a href="#">Blog</a>
            </nav>
        )
    }
}

export default Header;