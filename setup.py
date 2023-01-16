from setuptools import setup

setup(
    name="putas",
    version="0.0.1",
    description="Useful module making Python easier",
    author="Kuba Jazdzyk",
    author_email="jazdzyk.kuba@gmail.com",
    packages=["putas", "putas.structs", "putas.task_master", "putas.task_master.extras"],
    entry_points={
        "console_scripts": [
            "task_master=putas.task_master.master:run",
            "task_master-start=putas.task_master.start:create_project_structure"
        ],
    }
)
