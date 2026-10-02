from database import new_session, TaskModel
from schemas import STaskAdd, STask
from sqlalchemy import select


class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:

            task_dict = data.model_dump()
            task = TaskModel(**task_dict)

            session.add(task)

            await session.flush()
            await session.commit()

            return task.id


    @classmethod
    async def find_all(cls) -> list[STask]:
        async with new_session() as session:
            query = select(TaskModel)

            result = await session.execute(query)

            task_models = result.scalars().all()

            return task_models


    


