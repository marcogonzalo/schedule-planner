import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';

import { API_URL } from '../../utils/common';

export const CourseTypeListPage = () => {
    const [courseTypeList, setCourseTypeList] = useState([]);

    const handleRemove = (id) => {
        fetch(`${API_URL}/course-types/${id}`, { method: 'DELETE' })
            .then(response => {
                if (response.status == 205) {
                    const newList = courseTypeList.filter((item) => item.id !== id);
                    setCourseTypeList(newList);
                }
            });
    };

    useEffect(() => {
        fetch(`${API_URL}/course-types`)
            .then(response => response.json())
            .then(data => {
                setCourseTypeList(data);
            });
    }, []);

    return (
        <Container>
            <h1>Course Types</h1>
            {courseTypeList && courseTypeList.map((ct) => (
                <Row key={ct.id}>
                    <Col xs={6} md={9}>
                        <Row>
                            <Col md={8}><strong>{ct.name}</strong></Col>
                            <Col
                                md={4}
                                className="text-start text-md-center"
                            >
                                {ct.duration} days
                            </Col>
                        </Row>                
                    </Col>
                    <Col xs={6} md={8} className="text-end">
                        <Link to={`${ct.id}/edit`}>
                            <a className="btn btn-primary">Edit</a>
                        </Link>
                        {' '}
                        <Button
                            variant="outline-danger"
                            onClick={() => handleRemove(ct.id)}
                        >
                            Remove
                        </Button>
                    </Col>
                </Row>
            ))}
        </Container>
    );
}
