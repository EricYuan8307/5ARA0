# Realtor Project (Weeks 2-3)

This repository contains the assignments for the Realtor project (weeks 2 and 3). In the Realtor project you will develop an application that assists realtors in valuating housing prices in the state of California. This project is split in two parts, where each part corresponds with one week of the course. Before you start the assignments, you will need to have Git, GitHub and VSCode properly installed. If not, please follow the getting started guide.


## Clone the Repository

Accept the assignment invitation in GitHub Classroom. This creates a new personal remote with the skeleton code for the Realtor project. Start VSCode, and in a terminal window, navigate to the root directory where you want to download the assignment repository. Then clone the repository, `git clone git@github.com:tue-5ARA0-<YYYY-QQ>/realtor-<YOUR GITHUB HANDLE>.git Realtor`, where you insert the correct year, quartile and your own GitHub handle. This command will download the assignment repository in a new `Realtor` directory. In VSCode, select `File > Open Folder...` and select the `Realtor` directory to open the downloaded project in VSCode.


## Activate and Initialize a Virtual Environment

A Virtual Environment creates a custom package-versioning environment for your specific Python project. This way, package versions of other projects do not interfere with your current project, and your runtime environment (including bugs) can be replicated across machines. In this course we use Anaconda to manage virtual environments and packages. The required package versions for the Realtor project are defined in the `environment.yml` file.

Open the Realtor project in VSCode and open a new terminal. Create a new virtual environment and install required packages by typing `conda env create -f environment.yml` (this might take a while). This command will create a new `realtor39` virtual environment. Activate the newly created environment by `conda activate realtor39`. Any package that is installed (`conda install <package>`) will now be added to the `realtor39` environment.

The Virtual Environment can be deactivated by typing `conda deactivate`. The Virtual Environment only needs to be created once, but you may be required to reactivate it when reopening your project. Look for the prompt prefix that indicates the active Virtual Environment, and reactivate if needed.


## Start the Jupyter Notebook

In the VSCode file explorer, double click on `realtor_week_2.ipynb` to start with the assignments. With the Jupyter extension installed (see getting started guide), this will directly open the notebook in VSCode.