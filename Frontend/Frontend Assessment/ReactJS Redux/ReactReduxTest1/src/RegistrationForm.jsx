import React, { useState } from 'react';
import useFormValidation from './useFormValidation';
import './RegistrationForm.css';

const RegistrationForm = () => {
    const [registeredStudents, setRegisteredStudents] = useState([]);

    const { values, errors, handleChange, handleSubmit, resetForm } = useFormValidation({
        initialValues: {
            email: '',
            password: '',
            retypePassword: '',
            firstName: '',
            lastName: '',
            phoneNumber: '',
            address: '',
            town: '',
            region: '',
            postcode: '',
            country: ''
        },
        validate: (values) => {
            const errors = {};
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            const passwordRegex = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{8,}$/;

            if (!values.email) {
                errors.email = 'Email is required';
            } else if (!emailRegex.test(values.email)) {
                errors.email = 'Invalid email format';
            }

            if (!values.password) {
                errors.password = 'Password is required';
            } else if (!passwordRegex.test(values.password)) {
                errors.password = 'Password must be at least 8 characters long, contain at least one number, one uppercase and one lowercase letter';
            }

            if (values.retypePassword !== values.password) {
                errors.retypePassword = 'Passwords do not match';
            }

            if (!values.firstName) {
                errors.firstName = 'First Name is required';
            }

            if (!values.lastName) {
                errors.lastName = 'Last Name is required';
            }

            if (!values.phoneNumber) {
                errors.phoneNumber = 'Phone Number is required';
            }

            if (!values.address) {
                errors.address = 'Address is required';
            }

            if (!values.region) {
                errors.region = 'Region is required';
            }

            if (!values.postcode) {
                errors.postcode = 'Postcode is required';
            }

            return errors;
        },
        onSubmit: (values) => {
            setRegisteredStudents([...registeredStudents, values]);
            console.log('Form submitted successfully:', values);
            resetForm();
        }
    });

    return (
        <div>
            <form onSubmit={handleSubmit}>
                <p1>Register here!</p1>
                <h2>USER REGISTRATION</h2>
                <p>Fields marked * are required.</p>

                <div>
                    <label>Email *</label>
                    <input type="email" name="email" value={values.email} onChange={handleChange} />
                    {errors.email && <p className="error">{errors.email}</p>}
                </div>

                <div>
                    <label>Password *</label>
                    <input type="password" name="password" value={values.password} onChange={handleChange} />
                    {errors.password && <p className="error">{errors.password}</p>}
                </div>

                <div>
                    <label>Re-Enter Password *</label>
                    <input type="password" name="retypePassword" value={values.retypePassword} onChange={handleChange} />
                    {errors.retypePassword && <p className="error">{errors.retypePassword}</p>}
                </div>

                <div>
                    <label>First Name *</label>
                    <input type="text" name="firstName" value={values.firstName} onChange={handleChange} />
                    {errors.firstName && <p className="error">{errors.firstName}</p>}
                </div>

                <div>
                    <label>Last Name *</label>
                    <input type="text" name="lastName" value={values.lastName} onChange={handleChange} />
                    {errors.lastName && <p className="error">{errors.lastName}</p>}
                </div>

                <div>
                    <label>Phone Number *</label>
                    <input type="text" name="phoneNumber" value={values.phoneNumber} onChange={handleChange} />
                    {errors.phoneNumber && <p className="error">{errors.phoneNumber}</p>}
                </div>

                <div>
                    <label>Address *</label>
                    <input type="text" name="address" value={values.address} onChange={handleChange} />
                    {errors.address && <p className="error">{errors.address}</p>}
                </div>

                <div>
                    <label>Town</label>
                    <input type="text" name="town" value={values.town} onChange={handleChange} />
                </div>

                <div>
                    <label>Region *</label>
                    <input type="text" name="region" value={values.region} onChange={handleChange} />
                    {errors.region && <p className="error">{errors.region}</p>}
                </div>

                <div>
                    <label>Postcode / Zip *</label>
                    <input type="text" name="postcode" value={values.postcode} onChange={handleChange} />
                    {errors.postcode && <p className="error">{errors.postcode}</p>}
                </div>

                <div>
                    <label>Country *</label>
                    <select name="country" value={values.country} onChange={handleChange}>
                        <option value="United Kingdom">United Kingdom</option>
                        <option value="United States of America">United States of America</option>
                        <option value="Australia">Australia</option>
                        <option value="India">India</option>
                        <option value="Canada">Canada</option>
                        <option value="Russia">Russia</option>
                        <option value="China">China</option>
                    </select>
                </div>

                <button type="submit">Register</button>
            </form>

            <div className="registered-students">
                <h3>Registered Students</h3>
                <ul className="student-list">
                    {registeredStudents.map((student, index) => (
                        <li key={index}>
                            <p><strong>Name:</strong> {student.firstName} {student.lastName}</p>
                            <p><strong>Email:</strong> {student.email}</p>
                            <p><strong>Phone:</strong> {student.phoneNumber}</p>
                            <p><strong>Address:</strong> {student.address}, {student.town}, {student.region}, {student.postcode}, {student.country}</p>
                        </li>
                    ))}
                </ul>
            </div>
        </div>
    );
};

export default RegistrationForm;
