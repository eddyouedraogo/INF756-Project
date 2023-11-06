import { Routes, Route } from 'react-router-dom';
import ConfigurePage from './views/ConfigurePage';
import ReviewPage from './views/ReviewPage';
import SimulationPage from './views/SimulationPage';

function App() {
  return (
    <Routes>
      <Route path='/' element={<ConfigurePage />} />
      <Route path='/configure' element={<ConfigurePage />} />
      <Route path='/review' element={<ReviewPage />} />
      <Route path='/simulation' element={<SimulationPage />} />
    </Routes>
  );
}

export default App;
