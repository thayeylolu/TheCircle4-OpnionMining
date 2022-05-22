import './App.css'
import styled from 'styled-components'
import Sidebar from './components/Sidebar'
import RightSidebar from './components/RightSidebar'
import MainContent from './components/MainContent'
function App() {
	return (
		<Container>
			<MainContent />
			<RightSidebar />
		</Container>
	)
}

const Container = styled.div`
	display: flex;
	width: 100%;
	background: linear-gradient(to bottom right, white 0%, #e6e4ff 70%);
	border-radius: 2rem;
	box-sizing: border-box;
	@media screen and (min-width: 320px) and (max-width: 1080px) {
		flex-direction: column;
	}
`

export default App
