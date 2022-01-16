import React from "react";
import { BrowserRouter, Route, Routes } from "react-router-dom";
import ScrollToTop from "./component/scrollToTop";

import { Navbar } from "./component/navbar";
import { Footer } from "./component/footer";

import { Home } from "./pages/home";
import { CreateCourseTypePage } from "./pages/course-types/create-course-type-page";
import { EditCourseTypePage } from "./pages/course-types/edit-course-type-page";
import { NotFound } from "./pages/404";

import injectContext from "./store/appContext";
import { CourseTypeListPage } from "./pages/course-types/course-type-list-page";

//create your first component
const Layout = () => {
	//the basename is used when your project is published in a subdirectory and not in the root of the domain
	// you can set the basename on the .env file located at the root of this project, E.g: BASENAME=/react-hello-webapp/
	const basename = process.env.BASENAME || '';

	return (
		<div>
			<BrowserRouter basename={basename}>
				<ScrollToTop>
					<Navbar />
					<Routes>
						<Route exact path="/" element={<Home />} />
						<Route exact path="course-types">
							<Route index element={<CourseTypeListPage />} />
							<Route exact path="new" element={<CreateCourseTypePage />} />
							<Route exact path=":courseTypeId">
								<Route exact path="edit" element={<EditCourseTypePage />} />
							</Route>
						</Route>
						<Route path="*" element={<NotFound />} />
					</Routes>
					<Footer />
				</ScrollToTop>
			</BrowserRouter>
		</div>
	);
};

export default injectContext(Layout);
