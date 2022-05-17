import React from "react";
import styled from "styled-components";
import Navbar from "./Navbar";
import Profile from "./Profile";

function MainContent() {
  return (
    <Container>
      <Navbar />
      <SubContainer>
        <SectionOne>
            <Profile/>
            <Profile/>
            <Profile/>
        </SectionOne>

        <SectionOne>
            <Profile/>
            <Profile/>
            <Profile/>
        </SectionOne>
      </SubContainer>
    </Container>
  );
}

const Container = styled.div`
  width: 90%;
  background: linear-gradient(to bottom right, #e6e4ff 0%, thistle 70%);

  margin: 1rem 2rem 1rem 2rem;
  @media screen and (min-width: 320px) and (max-width: 1080px) {
    display: flex;
    flex-direction: column;
    width: 100%;
    margin: 1rem;
    padding 1rem;
  }
`;

const SubContainer = styled.div`
  margin: 0.5rem 0.5rem 0.5rem 0.5rem;
  padding: 1rem 1rem 1rem 1rem;
  height: 60%;
  width: 100%;
  display: flex;
  flex-direction: column;
  gap: 2rem;
  @media screen and (min-width: 320px) and (max-width: 1080px) {
    height: 100%;
  }
`;
const SectionOne = styled.div`
  display: flex;
  //justify-content: space-between; 
  height: 40%;
  gap: 1rem;
  margin: 3rem 2rem 3rem 1rem;
  width: 100%;
  @media screen and (min-width: 320px) and (max-width: 1080px) {
    flex-direction: column;
    align-items: center;
    height: max-content;
  }
`;
const ColumnOne1 = styled.div`
  display: flex;
  gap: 1rem;
  @media screen and (min-width: 320px) and (max-width: 1080px) {
    flex-direction: column;
    //justify-content: center;
    align-items: center;
    gap: 1rem;
    width: 100%;
  }
`;

const ColumnTwo1 = styled.div`
  display: flex;
  flex-direction: column;
  height: 115%;
  width: 100%;
  @media screen and (min-width: 320px) and (max-width: 1080px) {
    height: max-content;
    justify-content: center;
    align-items: center;
  }
`;

const TitleText1 = styled.p`
  span {
    font-weight: 500;
    color: #484258;
  }
  @media screen and (min-width: 320px) and (max-width: 1080px) {
    margin-top: 1rem;
  }
`;

const TitleText = styled.h3`
  height: 20%;
  /* padding-top */
`;

const SectionTwo = styled.div`
  display: flex;
  gap: 2rem;
  height: 26vh;
  @media screen and (min-width: 320px) and (max-width: 1080px) {
    flex-direction: column;
    height: max-content;
    width: 50%;
  }
`;
const ColumnOne2 = styled.div`
  @media screen and (min-width: 320px) and (max-width: 1080px) {
    display: flex;
    justify-content: center;
    align-items: center;
    flex-direction: column;
    width: 100%;
  }
`;

export default MainContent;
