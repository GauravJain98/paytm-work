To run
python venv myvenv
source myvenv/Scripts/activate
pip install flask
python app.py


#app.py is ignored

#to re write:
git update-index --no-skip-worktree app.py

#to re ignore
git update-index --skip-worktree app.py

#get list of ignored files
git ls-files -v . | grep ^S