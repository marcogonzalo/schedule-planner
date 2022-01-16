import React from 'react';
import { CourseTypeForm } from '../../component/course-type-form';

export const CreateCourseTypePage = () => {
    return (
        <div className="container">
            <h1>Create a new course type</h1>
            <CourseTypeForm />
        </div>
    );
};
