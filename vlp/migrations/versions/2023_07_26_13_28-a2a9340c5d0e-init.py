"""init

Revision ID: a2a9340c5d0e
Revises: 
Create Date: 2023-07-26 13:28:09.418827

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a2a9340c5d0e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('vlp',
    sa.Column('id', sa.String(), nullable=False, comment='Идентификатор'),
    sa.Column('md', sa.ARRAY(sa.Float()), nullable=True, comment='Измеренная по стволу глубина, м'),
    sa.Column('tvd', sa.ARRAY(sa.Float()), nullable=True, comment='Вертикальная глубина, м'),
    sa.Column('casing_d', sa.Float(), nullable=True, comment='Данные по ЭК. Диаметр трубы, м'),
    sa.Column('tubing_d', sa.Float(), nullable=True, comment='Данные по НКТ. Диаметр трубы, м'),
    sa.Column('tubing_h_mes', sa.Float(), nullable=True, comment='Данные по НКТ. Глубина спуска НКТ, м'),
    sa.Column('pvt_wct', sa.Float(), nullable=True, comment='PVT. Обводненность, %'),
    sa.Column('pvt_rp', sa.Float(), nullable=True, comment='PVT. Газовый фактор, м3/т'),
    sa.Column('pvt_gamma_oil', sa.Float(), nullable=True, comment='PVT. Отн. плотность нефти'),
    sa.Column('pvt_gamma_gas', sa.Float(), nullable=True, comment='PVT. Отн. плотность газа'),
    sa.Column('pvt_gamma_wat', sa.Float(), nullable=True, comment='PVT. Отн. плотность воды'),
    sa.Column('pvt_t_res', sa.Float(), nullable=True, comment='PVT. Пластовая температура, C'),
    sa.Column('p_wh', sa.Float(), nullable=True, comment='Буферное давление, атм'),
    sa.Column('geo_grad', sa.Float(), nullable=True, comment='Градиент температуры, C/100 м'),
    sa.Column('h_res', sa.Float(), nullable=True, comment='Глубина Верхних Дыр Перфорации, м'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_vlp_id'), 'vlp', ['id'], unique=False)
    op.create_table('well_data',
    sa.Column('id', sa.String(), nullable=False, comment='Идентификатор'),
    sa.Column('q_liq', sa.ARRAY(sa.Float()), nullable=True, comment='Дебиты жидкости, м3/сут'),
    sa.Column('p_wf', sa.ARRAY(sa.Float()), nullable=True, comment='Забойное давление, атм'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_well_data_id'), 'well_data', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_well_data_id'), table_name='well_data')
    op.drop_table('well_data')
    op.drop_index(op.f('ix_vlp_id'), table_name='vlp')
    op.drop_table('vlp')
    # ### end Alembic commands ###
