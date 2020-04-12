
import React, { Component } from "react";
import SinglePost from "./SinglePost";
import "./SinglePost.css"

class SimplePost extends React.Component{
    constructor(props) {
        super(props)
        this.state = {data: null}
    }
    componentDidMount() {
        fetch("http://127.0.0.1:5000/")
      .then(response => response.json())
      .then(data => this.setState({data}))
    }

    callSinglePost () {
        if (this.state.data) {
        var posts_info = this.state.data;
        var each_post_info = posts_info.map((post) => <SinglePost props={post} />);
        return each_post_info;
        }
    }

    render() {
        if(this.state.data == null)
                return (<h2>No data found</h2>);
        else{
            console.log(this.callSinglePost())
          return (
            <div className="postsimple">
                    {this.callSinglePost()}
            </div>
          );
        } 
    }
}


export default SimplePost 