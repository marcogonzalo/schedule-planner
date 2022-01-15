import React from 'react';
import { useForm } from "react-hook-form";

import Button from 'react-bootstrap/Button';
import Form from 'react-bootstrap/Form';

export const CourseTypeForm = ({ data }) => {
	const { register, formState: { errors }, handleSubmit } = useForm();
    const onSubmit = (data) => {
        console.log("data", data);
    } 
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
