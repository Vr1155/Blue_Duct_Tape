import React from 'react';
import bannerImage from '../../assets/All Images/P3OLGJ1 copy 1.png'

const Header = () => {
    return (
        <div>
            <div className='md:flex items-center mb-12 px-6'>
                <div className="header-details md:w-3/5 tracking-wider ">
                    <h1 className='text-7xl w-auto md:w-5/6'>
                        One Step Closer  To Your <span className='custom-text text-7xl'>NEEDS</span>
                    </h1>
                    <p className='w-auto md:w-5/6 mt-6 leading-relaxed'>Explore thousands of policies that match your needs and get the information you require via call or text.</p>
                    <button className='custom-btn mt-4'>Get Started</button>
                </div>
                <div className="image-section md:w-1/2">
                    <img src={bannerImage} alt="" srcset="" />
                </div>
            </div>
        </div>
    );
};

export default Header;