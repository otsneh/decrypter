import React from 'react';
import ReactDOM from 'react-dom';
import Main from './main';

document.addEventListener('DOMContentLoaded', () => {
    ReactDOM.render(
        React.createElement(Main),
        document.getElementById('root')
    );
});
