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
import { setMouses, setObjectifStatus } from '../redux/reducers/LabyrinthReducer';
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
  const [inProgress, setInProgress] = useState(true);

  let nbMouseDeadExitFound = 0;

  const formatLogMessage = (mouse) => {
    const { id, health, mental, current_room, objective_consumed } = mouse;
    const messageText = `
    La souris ${id} a été mise à jour :
    - Santé: ${health}
    - Mental: ${mental}
    - Pièce actuelle: ${current_room}
    - Objectif consommé: ${objective_consumed ? `Oui` : `Non`}
  `;
    setMessage((prevMessage) => [messageText, ...prevMessage]);
  };

  const updateLabyrith = (data) => {
    dispatch(setMouses(data));
    dispatch(setObjectifStatus(data));
    formatLogMessage(data);
  };

  function exportLog() {
    const mywindow = window.open('', 'PRINT');
    mywindow.document.write(`<html><head><title>${document.title}</title>`);
    mywindow.document.write('</head><body >');
    mywindow.document.write(`<h1>${document.title.toUpperCase()} - Résultat de la simulation</h1>`);
    mywindow.document.write(document.getElementById('content').innerHTML);
    mywindow.document.write('</body></html>');

    mywindow.document.close(); // necessary for IE >= 10
    mywindow.focus(); // necessary for IE >= 10*/

    mywindow.print();
    mywindow.close();

    return true;
  }

  useEffect(() => {
    try {
      const payload = {
        mouses_intelligence: [
          {
            intelligence_id: process.env.REACT_APP_INTELLIGENCE_1,
            number_of_mouses: selectedSmart.length
          },
          {
            intelligence_id: process.env.REACT_APP_INTELLIGENCE_2,
            number_of_mouses: selectedStupid.length
          }
        ],
        labyrinth_id: selectedLabyrinth?.value,
        ruleSet_id: selectedRuleItems[0].id
      };
      console.log(payload);
      const size = selectedLabyrinth.label.split('-')[1].trim();
      const fetchDataAndInitializeMouseStatus = async () => {
        setLoading('loading');
        const result = await fetchLabyrinthBySize(size);
        setRooms(result);
        setLoading('finished');
        const socket = new WebSocket(`ws://localhost:8080/ws/sim/${size}/`);
        socket.onopen = () => {
          console.log('Successfully connected to simulation server.');
          setInProgress(true);
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
            case 'exit_found':
            case 'dead':
              nbMouseDeadExitFound += 1;
              if (nbMouseDeadExitFound === selectedStupid.length + selectedSmart.length) {
                setInProgress(false);
              }
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
        <Box textAlign='center'>
          <div
            style={{
              backgroundColor: '#ccc',
              overflowX: 'auto',
              height: '2vh',
              margin: '0'
            }}
          >
            {inProgress ? 'Simulation en cours ..' : 'Simulation terminé'}
          </div>
        </Box>
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
              id='content'
            >
              <TextContent>
                <ul style={{ fontSize: '15px' }}>
                  {message.map((item) => (
                    <li key={Math.random()}>{item}</li>
                  ))}
                </ul>
              </TextContent>
            </div>
            {!inProgress && (
              <Box textAlign='center' margin='xl'>
                <Button onClick={() => exportLog()} variant='secondary'>
                  Exporter le resultat
                </Button>
              </Box>
            )}
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
