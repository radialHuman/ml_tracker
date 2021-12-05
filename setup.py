from os import mkdir

# main folder
mkdir("project_folders")
with open('project_folders/.gitkeep', 'w') as fp:
    pass

# for py and ipynb files
mkdir("project_folders/notebooks")
with open('project_folders/notebooks/.gitkeep', 'w') as fp:
    pass

# for data at various stages of processing
mkdir("project_folders/data")
with open('project_folders/data/.gitkeep', 'w') as fp:
    pass

# raw data
mkdir("project_folders/data/raw")
with open('project_folders/data/raw/.gitkeep', 'w') as fp:
    pass

# cleaned data
mkdir("project_folders/data/cleaned")
with open('project_folders/data/cleaned/.gitkeep', 'w') as fp:
    pass

# extar data
mkdir("project_folders/data/other")
with open('project_folders/data/other/.gitkeep', 'w') as fp:
    pass

# outptu data if produced
mkdir("project_folders/data/output")
with open('project_folders/data/output/.gitkeep', 'w') as fp:
    pass

# reports, images, charts as by product of the ipynb files
mkdir("project_folders/reports")
with open('project_folders/reports/.gitkeep', 'w') as fp:
    pass

# documentation
mkdir("project_folders/documentation")
with open('project_folders/documentation/.gitkeep', 'w') as fp:
    pass

# to save models as pkl, json etc
mkdir("project_folders/model")
with open('project_folders/model/.gitkeep', 'w') as fp:
    pass

# for secret key etc
mkdir("project_folders/configuration")
with open('project_folders/model/.gitkeep', 'w') as fp:
    pass

# for streamlit
mkdir("project_folders/ui")
with open('project_folders/model/.gitkeep', 'w') as fp:
    pass
