#include "6.h"

#include <filing.h>

#include <iostream>
#include <unordered_set>

struct Position {
  int i;
  int j;

  bool operator==(const Position& other) const {
    return (this->i == other.i) && (this->j == other.j);
  }
};

template <>
struct std::hash<Position> {
  std::size_t operator()(const Position& pos) const {
    return pos.i * 150 + pos.j;
  }
};

struct Direction {
  int v;
  int h;
};

Position get_next_position(const Position& current,
                           const Direction& direction) {
  return Position{current.i + direction.v, current.j + direction.h};
}

Direction get_next_direction(const Direction& direction) {
  return Direction{direction.h, -1 * direction.v};
}

class Map {
 private:
  std::vector<std::string> m_data;
  Position m_start_pos;
  int m_height;
  int m_width;

 public:
  Map() {
    operate_on_lines(6, [&](std::string line) { m_data.push_back(line); });
    m_height = (int)m_data.size();
    m_width = (int)m_data[0].size();

    for (int i = 0; i < m_height; ++i) {
      for (int j = 0; j < m_width; ++j) {
        char curr_char = m_data[i][j];

        if (curr_char != '^') {
          continue;
        }

        m_start_pos = {(int)i, (int)j};
        return;
      }
    }
    throw std::runtime_error("Expected Position");
  }

  const Position& get_start() const { return m_start_pos; }

  bool position_within_map(const Position& position) {
    return position.i >= 0 && position.i < m_height && position.j >= 0 &&
           position.j < m_width;
  }

  inline std::pair<Position, Direction> next_state(const Position& current,
                                                   const Position& next,
                                                   const Direction& direction) {
    if (m_data[next.i][next.j] == '#') {
      return std::make_pair(current, get_next_direction(direction));
    }
    return std::make_pair(next, direction);
  }

  void iterate_through(std::function<bool(const Position&, Direction&)> fn) {
    Position position = get_start();
    Direction direction = Direction{-1, 0};

    while (true) {
      if (fn(position, direction)) {
        break;
      }

      Position next_pos = get_next_position(position, direction);
      if (!position_within_map(next_pos)) {
        break;
      }

      auto [new_position, new_direction] =
          next_state(position, next_pos, direction);

      position = new_position;
      direction = new_direction;
    }
  }

  char change_pos(const Position& position, char change) {
    char original = m_data[position.i][position.j];
    m_data[position.i][position.j] = change;
    return original;
  }

  int count_x() {
    int total = 0;

    for (std::string s : m_data) {
      for (char c : s) {
        if (c == 'X') {
          total += 1;
        }
      }
    }

    return total;
  }
};

void six_a() {
  Map map;
  map.iterate_through([&](const Position& pos, Direction& dir) {
    map.change_pos(pos, 'X');
    return false;
  });

  std::cout << map.count_x() << "\n";
}

void six_b() {
  Map map;
  std::unordered_set<Position> passed_states;

  map.iterate_through([&](const Position& pos, Direction& dir) {
    passed_states.insert(pos);
    return false;
  });

  int infinite_loop_count = 0;
  for (const Position& obstacle_position : passed_states) {
    char original = map.change_pos(obstacle_position, '#');

    if (original == '^') {
      map.change_pos(obstacle_position, original);
      continue;
    }

    std::unordered_map<Position, std::vector<Direction>> history;

    map.iterate_through([&](const Position& pos, Direction& dir) {
      for (const Direction& old_dir : history[pos]) {
        if (old_dir.h == dir.h && old_dir.v == dir.v) {
          ++infinite_loop_count;
          std::cout << infinite_loop_count << "\n";
          return true;
        }
      }
      history[pos].push_back(dir);
      return false;
    });
    map.change_pos(obstacle_position, original);
  }

  std::cout << infinite_loop_count << "\n";
}

void six() { six_b(); }