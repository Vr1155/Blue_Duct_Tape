import React from 'react';
import SingleCategory from '../SingleCategory/SingleCategory';

const JobCategory = ({ category }) => {
    // console.log(category);
    return (
        <div className='text-center my-6'>
            <h1 className='text-5xl custom-text p-4'>Benefits Just for You—Free!</h1>
            <p className='text-lg mt-4'>We will ensure you are informed about all available benefits through a personal call and provide assistance throughout the application process.</p>
            <div className="grid md:grid-cols-4 gap-4 p-2 mt-4">
                {
                    category.map((ct) => <SingleCategory
                        key={ct.id}
                        ct={ct}
                    >
                    </SingleCategory>)
                }
            </div>
        </div>
    );
};

export default JobCategory;