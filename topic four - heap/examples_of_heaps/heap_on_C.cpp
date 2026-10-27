#include <iostream>
#include <vector>
#include <string>


class MaxHeap
{
    protected:
        std::vector<int> data;

        void shift_up(unsigned int ind_el)
        {
            int ind_son = ind_el;

            while((ind_son > 0) && (data[ind_son] > data[ind_son/2]))
            {
                std::swap(data[ind_son], data[ind_son/2]);
                ind_son /= 2;
            }
        }

        unsigned int ind_max_child(unsigned int ind_el)
        {
            std::vector<int>::iterator it_heap = data.begin();

            if(ind_el * 2 + 2 > data.size() - 1)
            {
                return ind_el * 2 + 1;
            }
            if(*(it_heap + ind_el * 2 + 1) > *(it_heap + ind_el * 2 + 2))
            {
                return ind_el * 2 + 1;
            }

            return ind_el * 2 + 2;
        }

        void shift_down(unsigned int ind_el)
        {
            int ind_par = ind_el;

            while((ind_par * 2 + 1 <= data.size() - 1))
            {
                unsigned int max_son_ind = this->ind_max_child(ind_par);
                
                if(data[ind_par] < data[max_son_ind])
                {
                    std::swap(data[ind_par], data[max_son_ind]);
                    ind_par = max_son_ind;
                }
                else
                {
                    break;
                }
            }
        }
    
    public:
        MaxHeap() {}

        void clear()
        {
            data.clear();
        }

        void insert(int new_el)
        {
            data.push_back(new_el);
            this->shift_up(data.size() - 1);
        }

        int get_max()
        {
            if(not(this->is_empty()))
            {
                return data[0];
            }
            else
            {
                std::cerr << "ERROR, heap is empty \n";
            }
        }

        int extract()
        {
            if(not(this->is_empty()))
            {
                int del_max = data[0];
                data[0] = data.back();
                data.pop_back();
                this->shift_down(0);
                return del_max;
            }
            else
            {
                std::cerr << "ERROR, heap is empty \n";
            }
        }

        bool is_empty()
        {
            return data.empty();
        }
};


int main()
{
    MaxHeap h;
    int x;
    std::string command;

    while(std::cin >> command)
    {
        if(command == "CLEAR")
        {
            h.clear();
        }
        else 
        {
            if(command == "INSERT")
            {
                std::cin >> x;
                h.insert(x);
            }
            else 
            {
                if(command == "DELMAX")
                {
                    std::cout << h.extract() << std::endl;
                }
                else
                {
                    if(command == "MAX")
                    {
                        std::cout << h.get_max() << std::endl;
                    }
                }
            }
        }  
    }

    return 0;
}