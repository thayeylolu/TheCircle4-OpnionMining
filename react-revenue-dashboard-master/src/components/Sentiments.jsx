import React from "react";
import styled from "styled-components";
import Badge from "./Badge";
import { cardShadow, hoverEffect, themeColor } from "../utils";

function Sentiments() {
  return (
    <InfoCard>
      <Card>
        <CardContent>
          <Row>
            <Digit>40%</Digit>
            <InfoContainer>
              <Title>Positive</Title>
              <SubTitle>In top 20%</SubTitle>
            </InfoContainer>
          </Row>
        </CardContent>
      </Card>
      <Card>
        <CardContent>
          <Row>
            <Digit>20%</Digit>
            <InfoContainer>
              <Title>Neutral</Title>
              <SubTitle>In top 20%</SubTitle>
            </InfoContainer>
          </Row>
        </CardContent>
      </Card>
      <Card>
        <CardContent>
          <Row>
            <Digit>40%</Digit>
            <InfoContainer>
              <Title>Negative</Title>
              <SubTitle>In top 20%</SubTitle>
            </InfoContainer>
          </Row>
        </CardContent>
      </Card>
      <Card>
        <CardContent>
          <Row>
            <Digit>32</Digit>
            <InfoContainer>
              <Title>Hashtags</Title>
              <SubTitle>Top 2</SubTitle>
            </InfoContainer>
          </Row>
          <Row justify>
            <Badge content="mobile app" glow />
            <Badge content="branding" glow />

          </Row>
        </CardContent>
      </Card>
      
    </InfoCard>
  );
}

const InfoCard = styled.div`

  width: 80%;
  background-color: white;
  border-radius: 1rem;
  padding: 2rem;
  margin-bottom: 1rem;
  margin-top: 1rem;
  color: white;
  box-shadow: ${cardShadow};
  transition: 0.4s ease-in-out;
  &:hover {
    box-shadow: ${hoverEffect};
  }
  @media screen and (min-width: 320px) and (max-width: 560px) {
    width: 70%;
    
  }
`;

const Card = styled.div`
  background-color: rgba(183, 194, 243, 0.3);
  border-radius: 1rem;
  margin-bottom: 1rem;
`;

const CardContent = styled.div`
  padding: 0.8rem 1rem 0.5rem 1rem;
`;

const Row = styled.div`
  display: flex;
  align-items: center;
  margin-bottom: 0.4rem;
  ${({ justify }) =>
    justify &&
    `
      justify-content:space-around;
      width:90%
  `}
`;
const Digit = styled.div`
  background-color: ${themeColor};
  padding: 0.8rem 1rem;
  font-size: 0.6rem;
  border-radius: 1rem;
`;
const InfoContainer = styled.div`
  //margin-left: 0.6rem;
`;
const Title = styled.h3`
  color: black;
`;

const SubTitle = styled.h5`
  color: #333333;
  font-weight: normal;
`;

export default Sentiments;
