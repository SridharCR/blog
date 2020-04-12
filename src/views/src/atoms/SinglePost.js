import "./SinglePost.css"
import React, { Component } from "react";

class SinglePost extends React.Component{
    constructor(props){
        super(props)
    }
    render() {
        var each_post_data = this.props.props
        if(each_post_data != null)
        return (
            <div className = "SinglePost">
                <h2>{each_post_data.title}</h2>
                <h5>{each_post_data.body}</h5>
                <h6>{each_post_data.username}</h6>
                <h6>{each_post_data.created}</h6>
            </div>
        )
        else{
            return <h2>No data available</h2>
        }
    }
}

export default SinglePost