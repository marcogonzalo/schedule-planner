import React from "react";
import { Link } from "react-router-dom";

export const Navbar = () => {
	return (
		<nav className="navbar navbar-light bg-light">
			<div className="container">
				<Link to="/">
					<span className="navbar-brand mb-0 h1">Schedule planner</span>
				</Link>
				<Link to="course-types">
					<a className="btn btn-primary">Course types</a>
				</Link>
			</div>
		</nav>
	);
};