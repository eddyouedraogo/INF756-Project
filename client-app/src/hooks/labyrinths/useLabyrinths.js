import { useState, useEffect } from 'react';
import fetchLabyrinths from '../../services/labyrinths/labyrinths';

const useFetchLabyrinth = () => {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState('loading');
  const [error, setError] = useState(null);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const responseData = await fetchLabyrinths();
        setData(responseData);
        setLoading('finished');
      } catch (err) {
        setError(err);
        setLoading('finished');
      }
    };

    fetchData();
  }, []);

  return { data, loading, error };
};

export default useFetchLabyrinth;
