#include <iostream>
using namespace std;

struct room
{
    int left, right, people;
};

room rooms[5001];
bool isFull[5001];
int N, Q, X, Y, peopleIndex = 1;
string cmd;

int findIndex()
{
    int cnt = 0;
    for (int i = 1; i <= N; ++i)
    {
        if (isFull[i])
        {
            cnt = 0;
            continue;
        }

        if (++cnt == Y)
        {
            return i - Y + 1;
        }
    }
    return -1;
}

int main()
{
    ios::sync_with_stdio(0), cin.tie(0);
    cin >> N >> Q;
    while (Q--)
    {
        cin >> cmd >> X >> Y;

        if (cmd == "new")
        {
            int index = findIndex();

            if (index == -1)
            {
                cout << "REJECTED\n";
            }
            else
            {
                int right = index + Y - 1;

                for (int i = index; i <= right; ++i)
                {
                    isFull[i] = true;
                }

                rooms[peopleIndex++] = {index, right, X};
                cout << index << " " << right << "\n";
            }
        }
        else if (cmd == "in")
        {
            rooms[X].people += Y;
        }
        else
        {
            rooms[X].people -= Y;

            if (!rooms[X].people)
            {
                for (int i = rooms[X].left; i <= rooms[X].right; ++i)
                {
                    isFull[i] = false;
                }

                cout << "CLEAN " << rooms[X].left << " " << rooms[X].right << "\n";
            }
        }
    }
    return 0;
}