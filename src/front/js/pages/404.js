import React from "react";
import { Link } from "react-router-dom";

export const NotFound = () => (
    <div className="container">
        <h1>Not found</h1>
        <br />
        <Link to="/">
            <button className="btn btn-primary">Back home</button>
        </Link>
    </div>
);
