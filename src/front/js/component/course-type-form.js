import React from 'react';
import { useForm } from "react-hook-form";

import PropTypes from 'prop-types';

import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

import { API_URL } from '../utils/common';

export const CourseTypeForm = ({ data }) => {
	const { register, formState: { errors }, handleSubmit } = useForm();

    const onSubmit = (formData) => {
        const headers = new Headers({
            'Content-Type': 'application/json'
        })
        let path = `${API_URL}/course-types`;
        let method = 'POST';
        
        if (data?.id) {
            path = `${path}/${data.id}`;
            method = 'PUT';
        }
        
        fetch(path, {
            body: JSON.stringify(formData),
            headers, 
            method,
        })
            .then(response => response.json())
            .then(data => console.log(data));
    };

    return (
        <Form onSubmit={handleSubmit(onSubmit)}>
            <Form.Group className="mb-3">
                <Form.Label
                    id="course-type-name-label"
                    htmlFor="course-type-name"
                >
                    Name
                </Form.Label>
                <Form.Control
                    id="course-type-name"
                    name="course-type-name"
                    type="text"
                    defaultValue={data?.name}
                    {...register('name', { required: true })}
                />
                {errors.name && <span>This field is required</span>}
            </Form.Group>
            <Form.Group className="mb-3">
                <Form.Label
                    id="course-type-duration-label"
                    htmlFor="course-type-duration"
                >
                    Duration (in days)
                </Form.Label>
                <Form.Control
                    id="course-type-duration"
                    name="course-type-duration"
                    type="number"
                    defaultValue={data?.duration}
                    {...register('duration', {
                        required: true,
                        min: 1
                    })}
                />
                {errors.duration && <span>Should be greater than 0</span>}
            </Form.Group>
            <Button variant="primary" type="submit">Send</Button>
        </Form>
    );
}

CourseTypeForm.propTypes = {
    data: PropTypes.object
};

CourseTypeForm.defaultProps = {
    data: null,
};