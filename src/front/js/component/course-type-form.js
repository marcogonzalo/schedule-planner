import React from 'react';
import { useForm } from "react-hook-form";

import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

export const CourseTypeForm = ({ data }) => {
	const { register, formState: { errors }, handleSubmit } = useForm();
    const BACKEND_URL = process.env.BACKEND_URL + '/api';

    const onSubmit = (formData) => {
        const headers = new Headers({
            'Content-Type': 'application/json'
        })
        if (data?.id) {
            formData.id = data.id
            fetch(`${BACKEND_URL}/course-types/${data.id}`, {
                body: JSON.stringify(formData),
                headers, 
                method: 'PUT',
            })
        } else {
            fetch(`${BACKEND_URL}/course-types`, {
                body: JSON.stringify(formData),
                headers,
                method: 'POST',
            })
        } 
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
