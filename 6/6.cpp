#include "6.h"

#include <filing.h>

#include <iostream>

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
    return std::hash<int>()(pos.i) * 31 + std::hash<int>()(pos.j);
  }
};

struct Direction {
  int v;
  int h;
};

Position get_next_position(Position& current, Direction& direction) {
  return Position{current.i + direction.v, current.j + direction.h};
}

Direction get_next_direction(Direction& direction) {
  if (direction.v == -1 && direction.h == 0) {
    return Direction{0, 1};
  }
  if (direction.v == 0 && direction.h == 1) {
    return Direction{1, 0};
  }
  if (direction.v == 1 && direction.h == 0) {
    return Direction{0, -1};
  }
  if (direction.v == 0 && direction.h == -1) {
    return Direction{-1, 0};
  }
  throw std::runtime_error("Incorrect Direction");
}

class Map {
 private:
  std::vector<std::string> m_data;
  Position m_start_pos;

 public:
  Map() {
    operate_on_lines(6, [&](std::string line) { m_data.push_back(line); });
    for (size_t i = 0; i < m_data.size(); ++i) {
      for (size_t j = 0; j < m_data[0].size(); ++j) {
        char curr_char = m_data[i][j];

        if (curr_char != '^') {
          continue;
        }

        m_start_pos = Position{(int)i, (int)j};
        return;
      }
    }
    throw std::runtime_error("Expected Position");
  }

  const Position& get_start() const { return m_start_pos; }

  bool position_within_map(Position& position) {
    if (position.i >= (int)m_data.size() || position.i < 0) {
      return false;
    }

    if (position.j >= (int)m_data[0].size() || position.j < 0) {
      return false;
    }
    return true;
  }

  std::pair<Position, Direction> next_state(Position& current, Position& next,
                                            Direction& direction) {
    char next_char = m_data[next.i][next.j];
    if (next_char == '#') {
      return std::pair(current, get_next_direction(direction));
    }
    return std::pair(next, direction);
  }

  void iterate_through(std::function<bool(Position&, Direction&)> fn) {
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

  char change_pos(Position& position, char change) {
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
  map.iterate_through([&](Position& pos, Direction& dir) {
    map.change_pos(pos, 'X');
    return false;
  });

  std::cout << map.count_x() << "\n";
}

void six_b() {
  Map map;
  std::unordered_map<Position, bool> passed_states;

  map.iterate_through([&](Position& pos, Direction& dir) {
    passed_states[pos] = true;
    return false;
  });

  int infinite_loop_count = 0;
  for (auto kv : passed_states) {
    Position obstacle_position = kv.first;
    char original = map.change_pos(obstacle_position, '#');

    if (original == '^') {
      map.change_pos(obstacle_position, original);
      continue;
    }

    std::unordered_map<Position, std::vector<Direction>> history;

    map.iterate_through([&](Position& pos, Direction& dir) {
      for (auto old_dir : history[pos]) {
        if (old_dir.h == dir.h && old_dir.v == dir.v) {
          infinite_loop_count += 1;
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