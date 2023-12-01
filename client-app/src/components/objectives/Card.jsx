import { getObjectiveId } from '../../helpers/index';

export default function Card({ objective }) {
  const { id, name, description } = objective;
  const imageSource = `/objectives/${getObjectiveId(id)}`;
  return (
    <div style={{ display: 'flex', alignItems: 'center' }}>
      <img src={imageSource} alt={description} style={{ width: '20%', height: '20%' }} />
      <div style={{ marginLeft: '15px' }}>
        <h3>{name}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}
