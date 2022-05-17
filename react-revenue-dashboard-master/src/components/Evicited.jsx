import React from "react";
import styled from "styled-components";
import AvatarImage from "../assets/avatarImage2.jpg";
import AvatarImage2 from "../assets/avatarImage3.jpg";
import { cardShadow, hoverEffect, themeColor } from "../utils";

function Evicted() {
  return (
    <YourProjects>
      <Project>
        <Row justify>
        <Avatar>
          <img src={AvatarImage} alt="" />
        </Avatar>
        <Detail>
          <SubTitle>1 day remaining</SubTitle>
        </Detail>
        <Avatar>
          <img src={AvatarImage2} alt="" />
        </Avatar>
        <Detail>
        <SubTitle>5 days remaining</SubTitle>
        </Detail>
        </Row>
      </Project>
         <Project>
        <Row justify>
        <Avatar>
          <img src={AvatarImage} alt="" />
        </Avatar>
        <Detail>
          <SubTitle>1 day remaining</SubTitle>
        </Detail>
        <Avatar>
          <img src={AvatarImage2} alt="" />
        </Avatar>
        <Detail>
        <SubTitle>5 days remaining</SubTitle>
        </Detail>
        </Row>
      </Project>
         <Project>
        <Row justify>
        <Avatar>
          <img src={AvatarImage} alt="" />
        </Avatar>
        <Detail>
          <SubTitle>1 day remaining</SubTitle>
        </Detail>
        <Avatar>
          <img src={AvatarImage2} alt="" />
        </Avatar>
        <Detail>
        <SubTitle>5 days remaining</SubTitle>
        </Detail>
        </Row>
      </Project>
    </YourProjects>

  );
}

const YourProjects = styled.div`
  height: 26%;
  width: 85%;
  background-color: white;
  margin: 0rem 0rem 5rem 0rem;
  padding: 1rem;
  border-radius: 1rem;
  box-shadow: ${cardShadow};
  transition: 0.4s ease-in-out;
  &:hover {
    box-shadow: ${hoverEffect};
  }
  @media screen and (min-width: 320px) and (max-width: 1080px) {
    height: max-content;
    width: 75%;
    margin-top: 1rem;
  }
`;

const Project = styled.div`
  display: flex;
  align-items: center;
  margin-bottom: 0.3rem;
  padding-left: 0rem;
`;
const Avatar = styled.div`
  img {
    height: 4rem;
    width: 4rem;
    border-radius: 4rem;
  }
`;
const Detail = styled.div`
  margin-left: 1rem;
`;
const Title = styled.h3`
  font-weight: 500;
  @media screen and (min-width: 320px) and (max-width: 1080px) {
    font-size: 1rem;
  }
`;
const SubTitle = styled.h5`
  font-weight: 300;
`;
const AllProjects = styled.h5`
  text-align: end;
  color: ${themeColor};
  cursor: pointer;
`;


const Row = styled.div`
  display: flex;
  align-items: center;
  margin-bottom: 0.4rem;
  padding-left: 1.5rem;
  padding-bottom: 0.5rem;
  ${({ justify }) =>
    justify &&
    `
      justify-content:space-around;
      width:90%
  `}
  `;

export default Evicted;
