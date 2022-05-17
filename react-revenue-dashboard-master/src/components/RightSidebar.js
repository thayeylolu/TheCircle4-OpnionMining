import React from 'react'
import styled from 'styled-components'
import { RiHomeLine, RiFileCopyLine } from 'react-icons/ri'
import { FaWallet } from 'react-icons/fa'
import { AiOutlinePieChart } from 'react-icons/ai'
import Badge from './Badge'
import AvatarImage from '../assets/avatarImage.jpeg'
import { darkThemeColor, ContainerThemeColor } from '../utils'
import Senitments from './Sentiments'
import Evicted from './Evicited'

function RightSidebar() {
	return (
		<Container>
			<Senitments />
			<Title>Other HouseMates</Title>
			<Evicted />
		</Container>
	)
}

const Container = styled.div`
	width: 40%;
	height: 100% !important;
	border-radius: 2rem;
	background-color:transparent;
	display: flex;
	padding:1rem;
	margin:1rem;
	flex-direction: column;
	align-items: center;
	gap: 2rem;
	@media screen and (min-width: 320px) and (max-width: 1080px) {
		width: 100%;
		height: max-content !important;
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

const LinksContainer = styled.div`
	background-color: ${ContainerThemeColor};
	height: 100%;
	width: 100%;
	border-radius: 2rem;
`

const Links = styled.ul`
	list-style-type: none;
	display: flex;
	flex-direction: column;
	padding-top: 2rem;
	height: 60%;
`

const Link = styled.li`
	margin-left: 25%;
	margin-bottom: 2rem;
	display: flex;
	gap: 1rem;
	color: #e4e4e4;
	cursor: pointer;
	h3 {
		font-weight: 300;
	}
	svg {
		font-size: 1.1rem;
		margin-top: 3%;
	}
`

const ContactContainer = styled.div`
	width: 25%;
	background-color: #091322;
	color: #c4c4c4;
	height: 15%;
	margin: auto auto;
	border-radius: 1rem;
	display: flex;
	flex-direction: column;
	padding: 1rem;

	a {
		color: white;
		text-decoration: none;
	}

	@media screen and (min-width: 320px) and (max-width: 1080px) {
		margin-bottom: 2rem;
	}
`
const Title = styled.h3`
	color: black;
`

export default RightSidebar
