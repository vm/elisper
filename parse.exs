defmodule Parse do
  def parse(text) do
    case as_variable text do
      :error -> case as_string text do
        :error -> case as_integer text do
          :error -> as_list text
          integer -> integer
        end
        string -> string
      end
      var -> var
    end
  end

  defp as_variable(text) do
    case text do
      "+" -> :add
      _ -> :error
    end
  end

  defp as_string(text) do
    quote_char = ~s(")
    cond do
      String.first(text) == quote_char and String.last(text) == quote_char ->
        String.slice(text, 1..-2)
      true -> :error
    end
  end

  defp as_integer(text) do
    case Integer.parse text do
      {int, ""} -> int
      _ -> :error
    end
  end

  defp as_list(text) do
    Enum.reduce Stream.unfold(text, &String.next_codepoint/1), {"", 0, []}, fn
      "(", {"" = empty, 0 = depth, []} ->
        {empty, depth + 1, []}
      " ", {temp, 1 = depth, sexps} ->
        {"", depth, sexps ++ [parse temp]}
      "(" = opening, {temp, 1 = depth, sexps} ->
        {temp <> opening, depth + 1, sexps}
      ")", {temp, 1, sexps} ->
        sexps ++ [parse temp]
      ")" = closing, {temp, depth, sexps} ->
        {temp <> closing, depth - 1, sexps}
      char, {temp, depth, sexps} ->
        {temp <> char, depth, sexps}
    end
  end
end
