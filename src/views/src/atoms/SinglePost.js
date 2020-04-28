import "./SinglePost.css"
import React, { Component } from "react";

class SinglePost extends React.Component {
    constructor(props) {
        super(props)
    }
    render() {
        var each_post_data = this.props.props
        if (each_post_data != null)
            return (
                <div className="SinglePost">
                    <div className="simpletitlebody">
                        <div className="title">{each_post_data.title}</div>
                        <div className="body">{each_post_data.body}</div>
                    </div>
                    <div className="simpleusercreated">
                        <div className="username">{each_post_data.username}</div>
                        <div className="created_by">{each_post_data.created}</div>
                    </div>
                </div>
            )
        else {
            return <h2>No data available</h2>
        }
    }
}

export default SinglePost