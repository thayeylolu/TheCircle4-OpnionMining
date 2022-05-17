import React from 'react'
import styled from 'styled-components'


const Emoji = props => (
    <div>
    <span
        className="emoji"
        role="img"
        aria-label={props.label ? props.label : ""}
        aria-hidden={props.label ? "false" : "true"}
    >
        {props.symbol}
    </span>
    </div>

    
);
export default Emoji;