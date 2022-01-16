import React, { useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import PropTypes from 'prop-types';

import { CourseTypeForm } from '../../component/course-type-form';

export const EditCourseTypePage = () => {
    const { courseTypeId } = useParams();
    const [courseType, setCourseType] = useState({});
    const API_URL = process.env.BACKEND_URL + '/api';

    useEffect(() => {
        fetch(`${API_URL}/course-types/${courseTypeId}`)
            .then(response => response.json())
            .then(data => {

                setCourseType(data)
            })
    }, [])

    return (
        <div className="container">
            <h1>Editing {courseType.name}</h1>
            <CourseTypeForm data={courseType} />
        </div>
    );
};

EditCourseTypePage.propTypes = {
    id: PropTypes.number,
}
