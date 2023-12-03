/* eslint-disable no-console */
/* eslint-disable camelcase */
/* eslint-disable no-case-declarations */
/* eslint-disable no-unused-vars */
/* eslint-disable no-prototype-builtins */
/* eslint-disable no-param-reassign */
/* eslint-disable no-continue */
/* eslint-disable no-restricted-syntax */
import React, { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import {
  Grid,
  SpaceBetween,
  Button,
  Box,
  Spinner,
  TextContent
} from '@cloudscape-design/components';
import { Link, useNavigate } from 'react-router-dom';
import CustumLayout from '../layout';
import { fetchLabyrinthBySize } from '../services/labyrinths/labyrinths';
import { setMouses } from '../redux/reducers/LabyrinthReducer';
import Labyrinth from '../components/labyrinths/Labyrinth';

export default function SimulationPage() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const selectedLabyrinth = useSelector((state) => state.labyrinth.selected);
  const selectedStupid = useSelector((state) => state.mouse.selected_stupid);
  const selectedSmart = useSelector((state) => state.mouse.selected_smart);
  const selectedRuleItems = useSelector((state) => state.rule.selected);
  const [rooms, setRooms] = useState([]);
  const [loading, setLoading] = useState(null);
  const [message, setMessage] = useState([]);

  const formatLogMessage = (mouse) => {
    const { id, health, mental, current_room } = mouse;
    const messageText = `
    La souris ${id} a été mise à jour :
    - Santé: ${health}
    - Mental: ${mental}
    - Pièce actuelle: ${current_room}
  `;
    setMessage((prevMessage) => [messageText, ...prevMessage]);
  };

  const updateLabyrith = (data) => {
    dispatch(setMouses(data));
    formatLogMessage(data);
  };

  useEffect(() => {
    try {
      const payload = {
        mouses_intelligence: [
          { intelligence_id: 4, number_of_mouses: selectedSmart.length },
          { intelligence_id: 1, number_of_mouses: selectedStupid.length }
        ],
        labyrinth_id: selectedLabyrinth?.value,
        ruleSet_id: selectedRuleItems[0].id
      };
      const size = selectedLabyrinth.label.split('-')[1].trim();
      const fetchDataAndInitializeMouseStatus = async () => {
        setLoading('loading');
        const result = await fetchLabyrinthBySize(size);
        setRooms(result);
        setLoading('finished');
        const socket = new WebSocket(`ws://localhost:8080/ws/sim/${size}/`);
        socket.onopen = () => {
          console.log('Successfully connected to simulation server.');
          socket.send(JSON.stringify(payload));
        };
        socket.onmessage = (e) => {
          const data = JSON.parse(e.data);
          switch (data.type) {
            case 'info':
              setMessage((prevMessage) => [data.message, ...prevMessage]);
              break;
            case 'mouse_status':
              updateLabyrith(data.mouse);
              break;
            default:
              break;
          }
        };
      };
      fetchDataAndInitializeMouseStatus();
    } catch (error) {
      console.error('Error fetching data:', error);
      navigate('/');
    }
  }, []);

  return (
    <CustumLayout>
      <SpaceBetween size='xxs'>
        <Grid gridDefinition={[{ colspan: 7 }, { colspan: 5 }]}>
          <div>
            {loading === 'finished' ? (
              <Labyrinth data={rooms} />
            ) : (
              <Box textAlign='center' margin={{ top: 'xxxl' }}>
                <Spinner size='large' />
              </Box>
            )}
          </div>
          <Box textAlign='center' margin={{ top: 'xxxl' }}>
            <div
              style={{
                backgroundColor: '#ccc',
                overflowX: 'auto',
                height: '50vh',
                margin: '0'
              }}
            >
              <TextContent>
                <ul style={{ fontSize: '15px' }}>
                  {message.map((item) => (
                    <li key={Math.random()}>{item}</li>
                  ))}
                </ul>
              </TextContent>
            </div>
          </Box>
        </Grid>
        <Box textAlign='center'>
          <Link to='/'>
            <Button>Quitter</Button>
          </Link>
        </Box>
      </SpaceBetween>
    </CustumLayout>
  );
}
