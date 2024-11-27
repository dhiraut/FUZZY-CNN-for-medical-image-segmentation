# How to Run
Clone the Repository

bash
Copy code
git clone https://github.com/your-username/fuzzy-cnn-segmentation.git
cd fuzzy-cnn-segmentation
Install Dependencies

bash
Copy code
pip install numpy matplotlib
Set the Image Path

Place your medical image in the repository folder.
Update the path in main.py:
python
Copy code
input_image = plt.imread('path/to/your/image.jpg')[:, :, 0]
Run the Program

bash
Copy code
python main.py
View Results

The segmentation outputs and metrics will be displayed.
