import React, { useEffect } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import Card from './Card';
import { fetchObjectivesbData } from '../../redux/actions/objectives';

export default function List() {
  const dispatch = useDispatch();
  const objectives = useSelector((state) => state.objectives.list);
  // const loading = useSelector((state) => state.objectives.loading);

  useEffect(() => {
    dispatch(fetchObjectivesbData());
  }, [dispatch]);

  return (
    <div>
      {objectives.map((objective) => {
        return (
          <div key={objective.id}>
            <Card objective={objective} />
          </div>
        );
      })}
    </div>
  );
}
