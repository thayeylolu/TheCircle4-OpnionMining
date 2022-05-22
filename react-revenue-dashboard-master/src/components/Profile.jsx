import React from "react";
import styled from "styled-components";
import Popups from "./Popups";
import AvatarImage from "../assets/michelle.jpeg";
import { themeColor} from "../utils";
import userData from "../users_data.json"
//import userData from "../userData"
import {useState} from 'react';



/* 
<Container>
        <ProfileContainer> 
        <Avatar src={AvatarImage} />
    
        <ButtonName>{data.Name}</ButtonName>

        <Emoji>
          <span>🙂&emsp;&emsp;</span>
          <span>😐&emsp;&emsp;</span>
          <span>😒&emsp;&emsp;</span>
        </Emoji>
      
          {
            data.sent.map(()=>{
                  return (
                    <SubTitle>
                      <Digit>5%&emsp;</Digit>
                      <Digit>&emsp;20%&emsp;</Digit>
                      <Digit>&emsp;15%&emsp;</Digit>
                    </SubTitle>
                  )
            })
          }
      
      </ProfileContainer>
      </Container>

*/

function Profile() {    
  return (
    <>
    {
    userData.map((data)=>{
        return (
          <Container>
        <ProfileContainer> 
        <Avatar src={AvatarImage} />
    
        <ButtonName>{data.Name}</ButtonName>

        <Emoji>
          <span>🙂&emsp;&emsp;</span>
          <span>😐&emsp;&emsp;</span>
          <span>😒&emsp;&emsp;</span>
        </Emoji>
        <SubTitle>
            {
            data.sent.map((likeData)=>{
                  return (
                    <>
                      <Digit>{likeData}%</Digit>
                    </>
                  )
            })
          }
        </SubTitle>
      </ProfileContainer>
      </Container>
        )
    })
  }
    </>
  )
}




const ProfileContainer = styled.div`
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
   align-items: center;
`;


const Avatar = styled.img`
	height: 7rem;
	border-radius: 6rem;
	margin-top: 2rem;
`

const Name = styled.h1`
	color: white;
	font-size: 1rem;
	font-weight: 400;
	margin: 0.8rem 0 0.5rem 0;
`
const Container = styled.div`
  background: #e6e4ff;
  padding-bottom: 2rem;
  border-radius:1rem;
  @media screen and (min-width: 320px) and (max-width: 1080px) {
    display: flex;
    flex-direction: column;
  }
`;

const PopCardContainer = styled.div`
  width: 0%;
  background: linear-gradient(to bottom right, white 0%, #e6e4ff 70%);
  border-bottom-right-radius: 2rem;
  border-top-right-radius: 2rem;
  margin: 1rem 2rem 1rem 4rem;
  @media screen and (min-width: 320px) and (max-width: 1080px) {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin: 0.5rem 0 0 0;
  }
`;



const Emoji = styled.h3`
    padding: 1rem  1rem 0rem 2.5rem;
    display: flex;
    flex-direction: row;

  span {
    font-weight: 200;
    color: #484258;
  }
  @media screen and (min-width: 320px) and (max-width: 1080px) {
    margin-top: 1rem;
  }
`;


const SubTitle = styled.h4`
    padding: 0rem;

  span {
    font-weight: 200;
    color: white;
  }
  @media screen and (min-width: 320px) and (max-width: 1080px) {
    margin-top: 1rem;
  }
`;

const ButtonName = styled.button`
  background-color: ${themeColor};
  border: 1rem;
  outline: none;
  margin: 1rem;
  padding: 0.5rem 1rem;
  color: white;
  border-radius: 0.5rem;
  font-size: 0.8rem;
  font-weight: normal;

`;

const Digit = styled.span`
  background-color: ${themeColor};
  padding: 0.2rem 0.7rem;
  font-size: 1rem;
  // border-radius: 1rem;
`;

export default Profile;