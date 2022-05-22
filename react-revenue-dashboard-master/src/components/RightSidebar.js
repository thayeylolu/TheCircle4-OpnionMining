import React from 'react'
import styled from 'styled-components'
import { RiHomeLine, RiFileCopyLine } from 'react-icons/ri'
import { FaWallet } from 'react-icons/fa'
import { AiOutlinePieChart } from 'react-icons/ai'
import Badge from './Badge'
import AvatarImage from '../assets/avatarImage.jpeg'
import { darkThemeColor, ContainerThemeColor } from '../utils'
import Sentiments from './Sentiments'
import Evicted from './Evicited'

function RightSidebar() {
	return (
		<Container>
			<Title></Title>
			<Title></Title>
			<Title></Title>
			<Title></Title>
			<Title></Title>
			<Title></Title>
			<Title></Title>
			<Title></Title>
			<Title>Sentiments Summary</Title>
			<Sentiments />
		</Container>
	)
}

const Container = styled.div`
	width: 40%;
	height: 100% !important;
	border-radius: 2rem;
	background-color: transparent;
	display: flex;
	padding: 1rem;
	//margin:1rem;
	flex-direction: column;
	justify-content: center;
	align-items: center;
	gap: 1rem;
	@media screen and (min-width: 320px) and (max-width: 1080px) {
		width: 100%;
		height: max-content !important;
		padding: 1rem 0;
	}
`

const ProfileContainer = styled.div`
	display: flex;
	justify-content: center;
	align-items: center;
	flex-direction: column;
`

const Avatar = styled.img`
	height: 7rem;
	border-radius: 6rem;
	margin-top: 20%;
`

const Name = styled.h1`
	color: white;
	font-size: 1.5rem;
	font-weight: 400;
	margin: 0.8rem 0 0.5rem 0;
`

const Title = styled.h3`
	color: black;
`

export default RightSidebar
