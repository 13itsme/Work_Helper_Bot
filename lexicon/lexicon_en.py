LEXICON_EN = {
    'start': (
        "Hey! I'm your personal helper bot. "
        "I can add, edit, and delete your notes.\n"
        "For more information, send me /help."
    ),
    'help': (
        "Here is the list of commands:\n"
        "/add - Add a new note\n"
        "/edit - Edit an existing note\n"
        "/delete - Delete a selected note\n"
        "/delete_all - Delete all notes\n"
        "/sum - Check the total sum of your notes\n"
        "/list - View your list of videos"
    ),
    'empty_add': (
        "It seems you sent /add without any information.\n"
        "Please use the format: /add [video's title] [cost in $]"
    ),
    'non_empty_add': (
        "✅ Video successfully added!\n"
        "Current total sum of all videos: {total}$"
    ),
    'sum': "💰 Current total sum of all videos: {total}$",
    'empty_delete': (
        "⚠️ I need more information to delete a video.\n"
        "Use the format: /delete [video's title]"
    ),
    'non_empty_delete': "🗑️ Video successfully deleted!",
    'list': "📄 Your list of videos: {videos_list}"
}
