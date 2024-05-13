# Building and deploying a containerized Streamlit app on AdaLab
This repository contains files and folders that define a Streamlit app (`pages/`, `utils/`, `0_🏡_Main page.py`, and `start_app.sh`) and a Containerfile (`Containerfile`) that specifies the build steps to build a container image for the Streamlit app. This README also contains instructions for building and deploying the Streamlit app in version 1.3.x of [AdaLab](https://adamatics.com/index.php/platform-2/).

This README can also be viewed in GitHub at: [https://github.com/adamatics/containerize-streamlit-app](https://github.com/adamatics/containerize-streamlit-app).

Click the video links to watch them.

## Template for an advanced Streamlit app

This repo contains a minimal working example of a multi-page, stateful Streamlit app.

### How to use the template
First, some tips on how to use the template for a Streamlit app:

- The main page of the Streamlit app is contained in `0_🏡_Main page.py`. Each additional page is contained in a separate file under `pages` (e.g., `pages/1_Page One.py`).
- If you need to use a different file as the main page, you must also modify the environment variable `MAIN_APP_FILE` in the `Containerfile`. 
- For repetitive use of functions, widgets or components, write them in a separate module and import them into the corresponding page file(s).
- The app is served on port `8501` by default. You can change this in `start_app.sh`.
- If you need additional packages (e.g., Pandas, Plotly), you need to explicitly install them in the `Containerfile`.
- You can store variables and widget states, and share them between pages using `st.session_state`. You can find some helper functions in `utils/utils.py`.
- You can use placeholders for widgets. You can store individual widgets as variables and modify the specific component at runtime.

## Structure of the rest of the README
In the following sections, we describe the steps required to deploy a Streamlit app as a containerized stand-alone app on [AdaLab](https://adamatics.com/index.php/platform-2/). In summary, the steps are as follows:

1. Build the container image.
2. Make the container image available in organization.
3. Deploy your Streamlit app.


# Build the container image
First, open a terminal, e.g. by going to your Lab, and make sure that the directory you are in is the folder that the repository was cloned into. You can check this by listing the files in your current directory with the command `ls` and making sure that you are seeing the expected files, as shown below:

[Use the `ls` command to check that expected files are there](https://www.veed.io/view/34c15a92-6634-49fc-8826-0a6ff6a99cf6?panel=share)

Then, from the terminal, build the container image with the below command:

```docker build -t my-app:0.1.0 . -f Containerfile```

The argument `-t my-app:0.1.0` specifies the name and tag to use for the built container image, and you can specify it as you wish. The only requirement is that a container image with this name does not already exist in your Lab and that the name follows the [Open Container Initiative (OCI) naming convention](https://github.com/containers/image/blob/main/docker/reference/regexp.go). The build process will look as shown below if you have built this image before. Otherwise, there will be some more steps in which the various components need to be downloaded to the local compute resource.

[Container image build process in the terminal](https://www.veed.io/view/70484d9c-b442-470d-89ad-41a8d3d1ee5a?panel=share)

# Make the container image available in your organization
Once the image building process is complete, you will have the container image available in your Lab on AdaLab. 

To share the container image with colleagues and make it available for app deployment, head over to the AdaLab menu and select the menu item "Container Images". Then click the "Publish New" button found to the right of the text "Container Images". Follow the steps in the wizard that pops up, choosing "App" as the Container Image Type in the first step and "Lab" as the source of the container image in the second step. In the third step, specify the unique name and version combination for the container image. In the fourth step, type in a human-friendly name and description for the container image and then click the "Publish" button. When the publishing process has finalized, click the "Refresh" button to make the options for published container images available.

[Share the container image for the app](https://www.veed.io/view/1c2faedc-1fc8-49a8-9742-ae431478fbcd?panel=share)

# Deploy your Streamlit app
To deploy your containerized Streamlit app, click "Deploy app" in the triple-dot menu on the right-hand side for the container image entry on the "Container Images" page. Fill out the fields with a name and description for the app and click the "Deploy App" button. You can view the logs for the deployment, and once the deployment has finished, go to the app by clicking the link for the app on the "App Deployment" page to which you are routed after clicking the "Deploy App" button. This process is shown below:

[Deploy the app](https://www.veed.io/view/b8a3d5a6-5538-4903-ab4a-d578d2859a47?panel=share)